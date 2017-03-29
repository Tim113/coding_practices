# VPC and subnets

_TL;DR_: Do this so you can't accidentally leave your database nodes open to attack.

A **VPC** (virtual private cloud) is the main container for all the instances set up on an AWS account.
This is a description of how we set up a VPC to have two **subnets** contained inside of it;
a **public** subnet that can freely communicate with the internet, and a **private** subnet
for which all communication must go through a **NAT gateway** (Network Address Translation gateway), which will be further explained.
The public subnet communicates with the internet through an **internet gateway**.
For this note, the internet gateway is the endpoint we're trying to reach for all communication paths.
Traffic is controlled between the subnets and gateways via **routing tables**.

[![What we are aiming for](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/images/nat-gateway-diagram.png)](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Scenario2.html)

This is the best practice outlined in [VPC Scenario 2](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Scenario2.html). For further information and if you have a lot of time (i.e. never) refer to the AWS docs on [VPC setup](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html).

## IP Addresses

An IP address such as `34.56.78.99` is an address which points to a server.

 - The IP address is split into two parts
   - A subnet
   - A host
     - For example, a subnet's address block is specified as `192.168.0.0/16`
     - This means that the subnet contains all hosts within range of `192.168.x.x`
     - the **/16** specifies the **subnet mask**.
     - `/16` translates to "when the IP address is translated to binary, the first
     16 `1`s are specified by the subnet"
     - This leaves the last 16 binary places to specify the host, i.e. there are
     `2^16 = 65536` host addresses avaible.

## Set up a VPC and Subnets

Whenever there is an instruction to "set up" some component of the system, it
should be easily visible on the AWS VPC sidebar

### Setup

 - Set up a VPC with a range of IP addresses
   - Example: `192.168.0.0/16`
   - `192.168.0.0/16` is the default for local communications with `65536` hosts available
 - Set up 2 subnets, one public, one private
 - The subnets should be associated to the VPC
   - The subnets could be:
      - `192.168.0.0/24` - public (still in a _private_ cloud though!)
      - `192.168.1.0/24` - private
   - This gives 255 addresses on each subnet
 - The public subnet should be able to communicate with the internet freely via an "Internet Gateway"
 - The private subnet must go though a "NAT gateway"
   - A NAT gateway is basically a one-way relay for messages to the internet gateway.

## NAT gateways

_TL;DR_: A NAT gateway lets nodes with no public IP address communicate with the internet.
The node leaves a request at the gateway.  The gateway makes the request to the internet,
awaiting the reply in the context of the private IP address that made the request.
The reply is forwarded back to the original private node via the gateway.

 - Nodes in the private subnet have no public IP address
 - If a private IP directly requests something from the internet, they won't be able to receive anything back
 - This is by design, so for example, a database node cannot be externally pinged
 - A malicious request has no direct entrypoint
   - The server it pings will have to try to send the message back to the public IP which doesn't exist
 - We do however, want the ability to make requests to the internet from the private node
   - Instead, the private node requests information from the NAT gateway
   - The gateway relays the request to the internet, receives the reply and passes it back to the private address
 - Thus the node can communicate with the internet via the gateway, however cannot be directly addressed if not via the gateway

## Internet gateways

_TL;DR_: This has to exist in your VPC, or the internet can't get out.

That is all. Except the internet isn't really trapped without one.

## Routing Tables

_TL;DR_: Subnets handle requests from different addresses differently.  Set up
a routing table for stuff happening in your private subnet, and one for stuff
happening in the public subnet.  Internal stuff is routed internally, private
stuff to the NAT and public requests go straight to the internet gateway.

 - Create two routing tables
   - One private
   - One public
 - Both routing tables redirect requests to the VPC locally
   - `Destination: 192.168.0.0/16 => Target: local`
   - Internal requests made using private IP addresses are redirected as normal
 - The public routing table redirects all other requests to the internet gateway
   - `Destination: 0.0.0.0/16 => Target: igw-xxxxxxxx`
 - The private routing table redirects all other request to the NAT gateway
   - `Destination: 0.0.0.0/16 => Target: nat-xxxxxxxxxxxxxxxxx`
 - For each routing table, click 'Subnet associations'
   - Associate the public routing table to the public subnet
   - Associate the private routing table to the private subnet

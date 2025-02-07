# IPv6 Subnet Visualizer

A web-based tool for visualizing IPv6 subnet allocations and bit boundaries. This tool helps network engineers understand IPv6 subnetting by providing a visual representation of network boundaries and address bits.

## Features

- Interactive visualization of IPv6 subnet boundaries
- Binary representation of network bits (positions 48-63)
- Display of network address and last address in full, uncompressed format
- Adjustable prefix length (48-64 bits)
- Network navigation within prefix boundaries
- Real-time updates as you modify inputs

## Technical Details

The application consists of:
- Flask backend for IPv6 calculations
- Interactive web frontend for visualization
- Support for standard IPv6 addressing features

### Address Handling

- Uses bits 48-63 of IPv6 addresses (subnet allocation space)
- Supports prefix lengths from /48 to /64
- Shows full, uncompressed IPv6 addresses
- Displays binary representation of relevant bits
- Indicates network boundaries through color coding


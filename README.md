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

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aibix0001/ipv6_visualizer.git
   cd ipv6_visualizer
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Using the Interface:
   - Enter an IPv6 address or use the default (2001:db8:abcd::)
   - Adjust the prefix length using the slider (48-64)
   - Use the navigation arrows to explore different networks within the prefix

## How It Works

### Input Processing

- Accepts IPv6 address input
- Validates prefix length (48-64)
- Calculates network boundaries

### Visualization

- Shows binary representation of bits 48-63
- Green background indicates bits within prefix
- Gray background for bits outside prefix
- Displays full network and last address

### Navigation

- Left/right arrows to navigate between networks
- Updates all displays in real-time
- Maintains prefix length while navigating

## Dependencies

- Python 3.x
- Flask
- ipaddress module

## License

MIT License

## Acknowledgments

This project was created with assistance from GitHub Copilot.
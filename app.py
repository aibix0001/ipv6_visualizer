from flask import Flask, render_template
import ipaddress

app = Flask(__name__)

DEFAULT_IPV6 = "2001:db8:abcd::"
DEFAULT_PREFIX = 56

@app.route('/')
def index():
    return render_template('index.html', default_ip=DEFAULT_IPV6, default_prefix=DEFAULT_PREFIX)

@app.route('/api/parse/<ipv6_str>/<int:prefix_len>')
def parse_ipv6(ipv6_str, prefix_len):
    try:
        # Validate prefix length
        if not 48 <= prefix_len <= 64:
            return {
                'status': 'error',
                'message': 'Prefix length must be between 48 and 64 bits'
            }

        # Validate IPv6 address and get network
        addr = ipaddress.IPv6Address(ipv6_str or DEFAULT_IPV6)
        network = ipaddress.IPv6Network(f'{addr}/{prefix_len}', strict=False)
        
        # Get binary representations
        network_binary = format(int(network.network_address), '0128b')
        last_addr_binary = format(int(network.broadcast_address), '0128b')
        relevant_network_bits = list(network_binary[48:64])
        relevant_last_bits = last_addr_binary[48:64]  # Last address bits
        
        # Change 0s to 1s only in the active prefix range
        for i in range(prefix_len - 48):
            if i >= 0 and i < len(relevant_network_bits):
                if relevant_network_bits[i] == '0':
                    relevant_network_bits[i] = '1'
        
        # Format network and last addresses with full representation
        network_addr = str(network.network_address).replace('::', ':0000:')
        while '::' in network_addr:
            network_addr = network_addr.replace('::', ':0000:')
        last_addr = str(network.broadcast_address).replace('::', ':0000:')
        while '::' in last_addr:
            last_addr = last_addr.replace('::', ':0000:')
            
        # Ensure each group has 4 digits
        network_parts = [f"{int(part, 16):04x}" if part else "0000" 
                        for part in network_addr.split(':')]
        last_parts = [f"{int(part, 16):04x}" if part else "0000" 
                     for part in last_addr.split(':')]
        
        return {
            'status': 'success',
            'binary': ''.join(relevant_network_bits),
            'last_addr_binary': relevant_last_bits,  # Changed to last address bits
            'prefix_len': prefix_len,
            'network': ':'.join(network_parts),
            'last_address': ':'.join(last_parts)
        }
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

if __name__ == '__main__':
    app.run(debug=True)

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

        # Validate IPv6 address
        addr = ipaddress.IPv6Address(ipv6_str or DEFAULT_IPV6)
        network = ipaddress.IPv6Network(f'{addr}/{prefix_len}', strict=False)
        
        # Convert to binary representation and extract bits 48-64
        binary = format(int(network.network_address), '0128b')
        relevant_bits = binary[48:64]  # Extract bits 48-64
        
        return {
            'status': 'success',
            'binary': relevant_bits,
            'prefix_len': prefix_len,
            'network': str(network.network_address),
            'broadcast': str(network.broadcast_address)
        }
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

if __name__ == '__main__':
    app.run(debug=True)

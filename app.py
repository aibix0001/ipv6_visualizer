from flask import Flask, render_template
import ipaddress

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/parse/<ipv6_str>/<int:prefix_len>')
def parse_ipv6(ipv6_str, prefix_len):
    try:
        # Validate IPv6 address
        addr = ipaddress.IPv6Address(ipv6_str)
        network = ipaddress.IPv6Network(f'{addr}/{prefix_len}', strict=False)
        
        # Convert to binary representation
        binary = ''.join(format(int(x, 16), '04b') for x in str(addr).replace(':', ''))
        
        return {
            'status': 'success',
            'binary': binary,
            'network': str(network.network_address),
            'broadcast': str(network.broadcast_address)
        }
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

if __name__ == '__main__':
    app.run(debug=True)

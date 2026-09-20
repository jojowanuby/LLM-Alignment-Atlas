import http.server,pathlib,urllib.parse
class H(http.server.BaseHTTPRequestHandler):
 def do_GET(self):
  if self.path.split('?')[0]=='/bridge':
   x=b"<script>let f=new URLSearchParams(location.search).get('f');let d=decodeURIComponent(location.hash.slice(1));fetch('/save?f='+encodeURIComponent(f),{method:'POST',body:d}).then(()=>document.body.innerText='saved '+d.length)</script>"
   self.send_response(200); self.send_header('Content-Type','text/html'); self.end_headers(); self.wfile.write(x)
  else:
   self.send_response(200); self.end_headers(); self.wfile.write(b'ok')
 def do_POST(self):
  q=urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query); f=q.get('f',['unnamed'])[0]
  n=int(self.headers.get('Content-Length','0')); b=self.rfile.read(n)
  pathlib.Path('/workspace/llm-alignment-chatgpt-free/raw/'+f).write_bytes(b)
  self.send_response(200); self.end_headers(); self.wfile.write(b'ok')
 def log_message(self,*a): pass
http.server.HTTPServer(('127.0.0.1',8765),H).serve_forever()

import sys
import subprocess
import json
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Conda Environments')

try:
  env_output = subprocess.check_output(['conda','env','list'])
  env_data = json.loads(env_output.decode())
  env_list = [env['name'] for env in env_data['envs']]
except Exception as e:
  print(e)
#except:
  env_list = ['No Environments']

label = QLabel('\n'.join(env_list), parent=window)

label.move(50,50)
window.show()
sys.exit(app.exec_())

import webbrowser
from time import sleep

TRAINING_URL = "https://nanikore7250.github.io/rlo/"  # TODO: 実際のURLに差し替え

print("installing...", end="", flush=True)
for i in range(1, 50):
    print("#", end="", flush=True)
    sleep(0.05)
print()

print("successfully installed!!!")
sleep(1)
print("本ファイルは研修用の無影響ファイルです。\n研修用Webページに移動します。")
sleep(1)
webbrowser.open(TRAINING_URL)

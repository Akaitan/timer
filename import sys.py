import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLCDNumber, QSlider, QGridLayout, QSpinBox
from PyQt5.QtCore import QTimer, QTime, Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class TimerApp(QWidget):
    def __init__(self):
        super().__init__()

        # ウィジェットの設定
        self.setWindowTitle("Timer App")
        self.setGeometry(100, 100, 300, 300)

        # タイマーの初期設定
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event)

        # レイアウトの設定
        layout = QGridLayout()

        # カウントダウン用のウィジェットを作成
        self.countdown = QLCDNumber(self)
        self.countdown.setDigitCount(7)
        layout.addWidget(self.countdown, 0, 0, 1, 3)

        # 設定時間のスピンボックスの設定
        self.time_spinbox = QSpinBox(self)
        self.time_spinbox.setRange(1, 60)
        layout.addWidget(self.time_spinbox, 1, 0)

        # スタートボタンの設定
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_event)
        layout.addWidget(self.start_button, 1, 1)

        # ストップボタンの設定
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_event)
        layout.addWidget(self.stop_button, 1, 2)

        # レイアウトの設定
        self.setLayout(layout)

        # カウントダウンの秒数を初期化
        self.seconds = 0

        # 音楽再生用の設定
        self.player = QMediaPlayer()
        self.player.setVolume(50)

    # タイマーイベント
    def timer_event(self):
        self.seconds -= 1
        self.countdown.display(self.seconds)
        if self.seconds == 0:
            self.timer.stop()
            # 音楽を再生する
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile("sound.mp3")))
            self.player.play()

    # スタートボタンイベント
    def start_event(self):
        self.timer.stop()
        self.seconds = self.time_spinbox.value() * 60
        self.countdown.display(self.seconds)
        self.timer.start(1000)

    # ストップボタンイベント
    def stop_event(self):
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer_app = TimerApp()
    timer_app.show()
    sys.exit(app.exec_())

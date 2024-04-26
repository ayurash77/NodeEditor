from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QBrush, Qt, QPen, QColor, QFont
from PySide6.QtWidgets import QGraphicsView, QGraphicsItem, QPushButton, QTextEdit

from node_graphics_scene import QDMGraphicsScene
from node_graphics_view import NodeGraphicsView


class NodeEditorWnd(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(NodeEditorWnd, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout()
        self.grScene = QDMGraphicsScene()

        self.view = NodeGraphicsView(self.grScene, self)
        self.layout.addWidget(self.view)
        self.setLayout(self.layout)

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Node Editor')
        self.setGeometry(800, 400, 800, 600)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Create graphics scene

        # Create graphics view

        self.add_debug_content()

        self.show()

    def add_debug_content(self):
        color_green1 = QColor('green')
        color_green2 = QColor('#98C279')
        green_brush1 = QBrush(color_green1)
        green_brush2 = QBrush(color_green2)
        outline_pen1 = QPen(QColor('#48B269'))
        outline_pen2 = QPen(color_green2)
        outline_pen1.setWidth(1)
        outline_pen2.setWidth(2)
        rect = self.grScene.addRect(-100, -100, 80, 100, outline_pen1, green_brush1)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        text = self.grScene.addText("Test Text", QFont('JetBrains Mono', 14))
        text.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        text.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

        widget1 = QPushButton("Test Button")
        proxy1 = self.grScene.addWidget(widget1)
        proxy1.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        proxy1.setPos(0, 30)

        widget2 = QTextEdit()
        proxy2 = self.grScene.addWidget(widget2)
        proxy2.setPos(0, 60)

        line = self.grScene.addLine(-100, -100, 80, -200, outline_pen2)
        line.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        line.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

import unittest

from manim import Scene, Square, Arc, PI, RED, UP, VGroup, Write, Text, PURPLE, RoundedRectangle


class MyTestCase(unittest.TestCase):
    def test_something(self):
        class TestScene(Scene):
            def construct(self):
                # 生成密钥
                key_text = Text("KEY", font_size=24, color=PURPLE)
                key_rect = RoundedRectangle(corner_radius=0.3, height=0.8, width=1.5, color=PURPLE, fill_opacity=0.2)
                key = VGroup(key_rect, key_text)

                # 加密动画 - 绘制锁图标
                lock_body = Square(side_length=0.4, color=RED, fill_opacity=0.5)
                lock_shackle = Arc(radius=0.2, angle=-PI, start_angle=PI, color=RED, stroke_width=3)
                lock_shackle.move_to(lock_body.get_top() + UP * 0.2)
                lock = VGroup(lock_body, lock_shackle).move_to(key, UP, )
                lock.set_opacity(opacity=0.2)

                self.play(Write(key), Write(lock), run_time=2)

        scene = TestScene()
        scene.render()


if __name__ == '__main__':
    unittest.main()

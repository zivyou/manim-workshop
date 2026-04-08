from manim import *

# 颜色定义
CYAN = "#00FFFF"
GOLD = "#FFD700"


class HTTPSFlow(Scene):
    def construct(self):
        # 设置场景
        self.camera.background_color = BLACK

        # 创建标题
        title = Text("HTTPS 握手流程", font_size=48, color=BLUE).to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # 创建 client 和 server 的视觉表示
        client_rect = RoundedRectangle(corner_radius=0.5, height=2, width=2.5, color=GREEN, fill_opacity=0.2)
        client_label = Text("Client", font_size=24, color=GREEN).next_to(client_rect, direction=UP, buff=0.2)
        client = VGroup(client_rect, client_label).move_to(LEFT * 4)

        server_rect = RoundedRectangle(corner_radius=0.5, height=2, width=2.5, color=ORANGE, fill_opacity=0.2)
        server_label = Text("Server", font_size=24, color=ORANGE).next_to(server_rect, direction=UP, buff=0.2)
        server = VGroup(server_rect, server_label).move_to(RIGHT * 4)

        # 添加端口标签
        port_label = Text("port:443", font_size=20, color=WHITE).next_to(server, DOWN)

        self.play(FadeIn(client), FadeIn(server), Write(port_label), run_time=1)
        self.wait(1)

        # 步骤 1: Client 向 Server 发起 HTTPS 请求
        step1_text = Text("步骤 1: Client 向 Server 的 443 端口发出 HTTPS 请求", font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(step1_text), run_time=1)

        request_arrow = Arrow(start=client.get_right(), end=server.get_left(), color=WHITE, buff=0.5)
        request_label = Text("HTTPS Request", font_size=16, color=WHITE).next_to(request_arrow, UP, buff=0.2)

        self.play(GrowArrow(request_arrow), Write(request_label), run_time=1)
        self.wait(2)

        # 清除箭头和文字
        self.play(FadeOut(request_arrow), FadeOut(request_label), FadeOut(step1_text), run_time=0.5)

        # 步骤 2: Server 返回 CA 证书
        step2_text = Text("步骤 2: Server 返回 CA 证书", font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(step2_text), run_time=1)

        # 创建证书的视觉表示
        cert_content = VGroup(
            Text("CA 证书", font_size=10, color=BLACK),
            Text("""
            • Server公钥
            • 证书签名
            • 颁发机构
            • 公司信息
            • 有效期
            """, font_size=8, color=BLACK),
            # Text("• 证书签名", font_size=6, color=WHITE),
            # Text("• 颁发机构", font_size=6, color=WHITE),
            # Text("• 公司信息", font_size=6, color=WHITE),
            # Text("• 有效期", font_size=6, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, center=True)


        cert_rect = RoundedRectangle(corner_radius=0.3, height=1.1, width=1, color=GOLD, fill_opacity=1.0)
        cert = VGroup(cert_rect, cert_content).move_to(server)

        cert_arrow = Arrow(start=server.get_left(), end=client.get_right(), color=GOLD, buff=0.5)
        cert_label = Text("返回证书", font_size=16, color=GOLD).next_to(mobject_or_point=cert_arrow, direction=UP, buff=0.2)

        self.play( GrowArrow(cert_arrow), Write(cert_label), MoveAlongPath(mobject=cert, path=cert_arrow), run_time=1.5)
        self.wait(2)

        # 清除箭头
        self.play(FadeOut(cert_arrow), FadeOut(cert_label), run_time=0.5)
        self.wait(1)

        # 步骤 3: Client 验证证书
        step3_text = Text("步骤 3: Client 验证证书有效性", font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(FadeOut(step2_text), Write(step3_text), run_time=1)

        # 验证过程的动画
        verify_checks = VGroup(
            Text("✓ 可信机构颁发", font_size=18, color=GREEN),
            Text("✓ 证书未过期", font_size=18, color=GREEN),
            Text("✓ 域名匹配", font_size=18, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(client, DOWN, buff=0.5)

        # 将证书移到 client 旁边
        self.play(cert.animate.move_to(client.get_center()), run_time=1)

        for check in verify_checks:
            self.play(Write(check), run_time=0.5)
            self.wait(0.3)

        self.wait(2)
        self.play(FadeOut(verify_checks), run_time=0.5)

        # 步骤 4: 从证书中提取 Server 公钥
        step4_text = Text("步骤 4: 从证书中提取 Server 公钥 A", font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(FadeOut(step3_text), Write(step4_text), run_time=0.5)

        # 提取公钥的动画
        pubkey_text = Text("公钥 A", font_size=24, color=CYAN)
        pubkey_rect = RoundedRectangle(corner_radius=0.3, height=0.8, width=2, color=CYAN, fill_opacity=0.2)
        pubkey = VGroup(pubkey_rect, pubkey_text).move_to(client.get_center())

        self.play(FadeOut(cert), FadeIn(pubkey), run_time=1)
        self.wait(1)
        self.play(FadeOut(step4_text), run_time=0.5)

        # 步骤 5: Client 生成随机密钥 KEY，用公钥加密并发送
        step5_text = Text("步骤 5: Client 生成随机密钥 KEY，用公钥 A 加密发送", font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(step5_text), run_time=1)

        # 生成密钥
        key_text = Text("KEY", font_size=24, color=PURPLE)
        key_rect = RoundedRectangle(corner_radius=0.3, height=0.8, width=1.5, color=PURPLE, fill_opacity=0.2)
        key = VGroup(key_rect, key_text).move_to(client.get_center())

        self.play(FadeIn(key), run_time=0.5)
        self.wait(1)

        # 加密动画 - 绘制锁图标
        lock_body = Square(side_length=0.4, color=RED, fill_opacity=0.5).next_to(key, RIGHT, buff=0.3)
        lock_shackle = Arc(radius=0.2, angle=-PI, start_angle=PI, color=RED, stroke_width=3)
        lock_shackle.move_to(lock_body.get_top() + UP * 0.2)
        lock = VGroup(lock_body, lock_shackle).move_to(key, ORIGIN)
        lock.set_opacity(0.2)
        encrypted_text = Text("加密后", font_size=16, color=RED).next_to(lock, DOWN)

        self.play(FadeOut(pubkey), Create(lock), Write(encrypted_text), run_time=0.5)

        # 将加密后的密钥发送给 server
        encrypted_key = VGroup(key.copy(), lock.copy()).move_to((client.get_right() + server.get_left()) / 2)

        send_arrow = Arrow(start=client.get_right(), end=server.get_left(), color=PURPLE, buff=0.5)
        send_label = Text("RSA(公钥A, KEY)", font_size=16, color=PURPLE).next_to(send_arrow, direction=UP, buff=0.2)

        self.play(GrowArrow(send_arrow), Write(send_label), run_time=1)
        self.wait(1)

        # 密钥到达 server
        self.play(encrypted_key.animate.move_to(server.get_center()), FadeOut(pubkey), run_time=1)
        self.wait(1)

        self.play(FadeOut(key), FadeOut(send_arrow), FadeOut(send_label), FadeOut(lock), FadeOut(encrypted_text), run_time=0.5)
        self.wait(1)

        # 步骤 6: Server 使用私钥解密 KEY
        step6_text = Text("步骤 6: Server 使用私钥解密 KEY", font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(FadeOut(step5_text), Write(step6_text), run_time=0.5)

        # 私钥解密动画
        privkey_text = Text("私钥", font_size=24, color=RED)
        privkey_rect = RoundedRectangle(corner_radius=0.3, height=0.8, width=1.5, color=RED, fill_opacity=0.2)
        privkey = VGroup(privkey_rect, privkey_text).next_to(server, DOWN, buff=1)

        self.play(FadeIn(privkey), run_time=0.5)

        # 解密动画 - 绘制解锁的锁图标
        unlock_lock_body = Square(side_length=0.4, color=GREEN, fill_opacity=0.5).move_to(encrypted_key.get_center())
        unlock_lock_shackle = Arc(radius=0.2, angle=-PI, start_angle=PI, color=GREEN, stroke_width=3)
        unlock_lock_shackle.move_to(unlock_lock_body.get_top() + UP * 0.2)
        unlock_lock = VGroup(unlock_lock_body, unlock_lock_shackle)
        unlock_text = Text("解密成功!", font_size=20, color=GREEN).next_to(unlock_lock, UP, buff=0.5)

        self.play(Create(unlock_lock), Write(unlock_text), run_time=0.5)
        self.wait(1)

        # 获取到 KEY
        key_received = VGroup(key_text.copy(), key_rect.copy()).move_to(server.get_center())
        self.play(Transform(encrypted_key, key_received), run_time=1)

        self.wait(1)
        self.play(FadeOut(privkey), FadeOut(unlock_lock), FadeOut(unlock_text), run_time=0.5)
        self.wait(1)


        # 步骤 7: 双方使用 KEY 进行加密通信
        step7_text = Text("步骤 7: 双方使用 KEY 进行加密通信", font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(FadeOut(step6_text), Write(step7_text), run_time=0.5)

        # 加密通信动画
        key_at_client = VGroup(key_text.copy(), key_rect.copy()).move_to(client.get_center())
        key_at_server = VGroup(key_text.copy(), key_rect.copy()).move_to(server.get_center())

        self.play(FadeOut(key_received), FadeIn(key_at_client), FadeIn(key_at_server), run_time=1)

        # 双向箭头表示加密通信
        comm_arrow_up = Arrow(start=client.get_right(), end=server.get_left(), color=BLUE, buff=0.5)
        comm_arrow_down = Arrow(start=server.get_left(), end=client.get_right(), color=BLUE, buff=0.5)
        comm_arrow_down.shift(DOWN * 0.3)

        self.play(GrowArrow(comm_arrow_up), GrowArrow(comm_arrow_down), run_time=1)
        self.wait(1)

        # 添加加密通信的消息示例
        msg_encrypted = Text("加密数据: AES(KEY,数据)", font_size=18, color=BLUE).next_to(comm_arrow_up, UP, buff=0.3)
        self.play(Write(msg_encrypted), FadeOut(step7_text), run_time=0.5)

        self.wait(2)

        # 总结
        summary = VGroup(
            Text("HTTPS 握手完成!", font_size=36, color=GOLD),
            Text("双方使用对称密钥 KEY 进行安全通信", font_size=24, color=WHITE)
        ).arrange(DOWN).to_edge(DOWN)

        self.play(Write(summary), run_time=1)
        self.wait(3)

        # 淡出所有元素，只保留标题
        self.play(
            FadeOut(client),
            FadeOut(server),
            FadeOut(encrypted_key),
            FadeOut(port_label),
            FadeOut(key),
            FadeOut(key_at_client),
            FadeOut(key_at_server),
            FadeOut(comm_arrow_up),
            FadeOut(comm_arrow_down),
            FadeOut(msg_encrypted),
            FadeOut(summary),
            run_time=2
        )

        # 最终标题
        final_title = Text("HTTPS 安全传输协议", font_size=60, color=BLUE)
        self.play(Transform(title, final_title), run_time=1)
        self.wait(2)


def main():
    """Main function to run the HTTPS flow visualization"""
    # 配置视频渲染参数
    config.quality = "high_quality"
    config.frame_rate = 30

    # 创建并渲染场景
    scene = HTTPSFlow()
    scene.render()


if __name__ == "__main__":
    main()
import unittest
from datetime import datetime

from trendradar.notification.senders import _build_feishu_payload


class TestBuildFeishuPayload(unittest.TestCase):
    def test_botbuilder_trigger_webhook_payload(self) -> None:
        now = datetime(2025, 12, 20, 12, 34, 56)
        payload = _build_feishu_payload(
            "https://www.feishu.cn/flow/api/trigger-webhook/xxx",
            batch_content="hello",
            report_type="当日汇总",
            total_titles=3,
            now=now,
        )

        self.assertEqual(payload["message_type"], "text")
        self.assertEqual(payload["content"]["total_titles"], "3")
        self.assertEqual(payload["content"]["timestamp"], "2025-12-20 12:34:56")
        self.assertEqual(payload["content"]["report_type"], "当日汇总")
        self.assertEqual(payload["content"]["text"], "hello")

    def test_feishu_bot_webhook_payload(self) -> None:
        now = datetime(2025, 12, 20, 12, 34, 56)
        payload = _build_feishu_payload(
            "https://open.feishu.cn/open-apis/bot/v2/hook/xxx",
            batch_content="hello",
            report_type="当日汇总",
            total_titles=3,
            now=now,
        )

        self.assertEqual(payload, {"msg_type": "text", "content": {"text": "hello"}})


if __name__ == "__main__":
    unittest.main()

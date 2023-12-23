# 编码人：TFY
# 时间：2022/6/4
import pytest

pytest.main(['--alluredir=historical_report/20231223_04', '-m=payment', '--reruns=2', '-n=2'])
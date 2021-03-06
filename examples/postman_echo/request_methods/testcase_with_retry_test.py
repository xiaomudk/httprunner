# NOTE: Generated By HttpRunner v3.1.4
# FROM: request_methods/testcase_with_retry.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from request_methods.request_with_retry_test import (
    TestCaseRequestWithRetry as RequestWithRetry,
)


class TestCaseTestcaseWithRetry(HttpRunner):

    config = (
        Config("request methods testcase: retry_whens")
        .variables(**{"app_version": "f1"})
        .base_url("https://postman-echo.com")
        .verify(False)
    )

    teststeps = [
        Step(
            RunTestCase("request with retry")
            .call(RequestWithRetry)
            .export(*["foo4"])
            .retry_whens()
            .assert_not_equal("$foo4", 3)
        ),
        Step(
            RunRequest("get with params")
            .get("/get")
            .with_params(**{"foo4": "${get_num()}"})
            .teardown_hook("${teardown_hook_sleep(1)}")
            .validate()
            .assert_equal("status_code", 200)
            .retry_whens()
            .assert_not_equal("body.args.foo4", "5")
        ),
    ]


if __name__ == "__main__":
    TestCaseTestcaseWithRetry().test_start()

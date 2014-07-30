import os
import time

from docker_plugin import tasks
from TestCaseBase import TestCaseBase


_IMAGE = 'http://localhost:8080'
_CMD = 'nc -nvl 8080 < tests/cloudify_docker_plugin/command &'


# Still under development
class TestUsingImage(TestCaseBase):
    def runTest(self):
        # TODO(Zosia) Change image to smaller one
        # TODO(Zosia) Change the command
        os.system(_CMD)
        time.sleep(1)
        self.ctx.properties['image_import'].update({'src': _IMAGE})
        self.ctx.properties['container_remove'].update({'remove_image': True})
        tasks.create(self.ctx)
        tasks.run(self.ctx)
        self._assert_container_running(self.assertTrue)

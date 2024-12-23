from bot import LOGGER, subprocess_lock
from bot.helper.ext_utils.status_utils import MirrorStatus, get_readable_file_size


class FFmpegStatus:
    def __init__(self, listener, gid, status=""):
        self.listener = listener
        self._gid = gid
        self._size = self.listener.size
        self.cstatus = status

    def gid(self):
        return self._gid

    def name(self):
        return self.listener.name

    def size(self):
        return get_readable_file_size(self._size)

    def status(self):
        if self.cstatus == "Convert":
            return MirrorStatus.STATUS_CONVERT
        if self.cstatus == "Split":
            return MirrorStatus.STATUS_SPLIT
        if self.cstatus == "Sample Video":
            return MirrorStatus.STATUS_SAMVID
        return MirrorStatus.STATUS_FFMPEG

    def task(self):
        return self

    async def cancel_task(self):
        LOGGER.info(f"Cancelling {self.cstatus}: {self.listener.name}")
        self.listener.is_cancelled = True
        async with subprocess_lock:
            if (
                self.listener.subproc is not None
                and self.listener.subproc.returncode is None
            ):
                self.listener.subproc.kill()
        await self.listener.on_upload_error(f"{self.cstatus} stopped by user!")

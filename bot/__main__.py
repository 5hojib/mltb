from asyncio import gather
from signal import SIGINT, signal

from .core.config_manager import Config

Config.load()

from . import LOGGER, bot_loop
from .core.handlers import add_handlers
from .core.mltb_client import TgClient
from .core.startup import (
    load_configurations,
    load_settings,
    save_settings,
    update_aria2_options,
    update_nzb_options,
    update_qb_options,
    update_variables,
)
from .helper.ext_utils.bot_utils import create_help_buttons, sync_to_async
from .helper.ext_utils.files_utils import clean_all, exit_clean_up
from .helper.ext_utils.jdownloader_booter import jdownloader
from .helper.ext_utils.telegraph_helper import telegraph
from .helper.listeners.aria2_listener import start_aria2_listener
from .helper.mirror_leech_utils.rclone_utils.serve import rclone_serve_booter
from .modules import (
    get_packages_version,
    initiate_search_tools,
    restart_notification,
)


async def main():
    await load_settings()
    await gather(TgClient.start_bot(), TgClient.start_user())
    await gather(load_configurations(), update_variables())
    await gather(
        sync_to_async(update_qb_options),
        sync_to_async(update_aria2_options),
        update_nzb_options(),
    )
    await gather(
        save_settings(),
        jdownloader.boot(),
        sync_to_async(clean_all),
        initiate_search_tools(),
        get_packages_version(),
        restart_notification(),
        telegraph.create_account(),
        rclone_serve_booter(),
        sync_to_async(start_aria2_listener, wait=False),
    )
    create_help_buttons()
    add_handlers()
    LOGGER.info("Bot Started!")
    signal(SIGINT, exit_clean_up)


bot_loop.run_until_complete(main())
bot_loop.run_forever()

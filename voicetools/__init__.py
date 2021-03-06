"""
Copyright 2018-2020 Jakub Kuczys (https://github.com/jack1142)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from redbot.core.bot import Red

from .voicetools import VoiceTools

__red_end_user_data_statement__ = (
    "This cog does not persistently store end user data."
    " This cog does store discord IDs as needed for operation.\n"
    "Discord IDs of users may occasionally be logged to file"
    " as part of debug logging."
)


async def setup(bot: Red) -> None:
    bot.add_cog(VoiceTools())

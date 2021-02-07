import sqlite3

import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from datetime import datetime


class Characters(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.conn = sqlite3.connect('./data/characters.db')
        # character information library
        self.c = self.conn.cursor()

    # add cog to main system
    @commands.Cog.listener()
    async def on_ready(self):
        print('Characters online')

    def find_character(self, char_name: str, var: str = '*'):
        self.c.execute(f"SELECT {var} FROM characters WHERE name = '{char_name}'")
        if var != '*':
            return self.c.fetchone()[0]
        else:
            return self.c.fetchone()

    @commands.command(hidden=True)
    @has_permissions(manage_guild=True)
    async def insert_character(self, *, param):
        # c.execute("INSERT INTO users VALUES (123456789, 0, 0)")
        self.c.execute(f"INSERT INTO characters VALUES ({param})")
        self.conn.commit()

    def find(self, var: str):
        self.c.execute(f'SELECT {var} FROM characters')
        return self.c.fetchall()

    def level_calc(self, xp: int):
        self.c.execute(f'SELECT total FROM xp')
        print(self.c.fetchall())


def setup(client):
    client.add_cog(Characters(client))

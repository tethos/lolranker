import os


class CogLoader:
    """
    Loads cogs for a bot from a directory.
    Raises Exception if directory doesn't exist or is empty (excluding __init__.py).
    """
    @staticmethod
    def load_cogs(bot, cogs_dir):
        if not os.path.exists(cogs_dir):
            raise FileNotFoundError(f'Error: cogs directory not found: {cogs_dir}')

        try:
            for filename in os.listdir(cogs_dir):
                if filename.endswith('.py') and filename != '__init__.py':
                    bot.load_extension(f'app.cogs.{filename[:-3]}')
                    print(f'Loaded {filename[:-3]}')
        except Exception as e:
            print(f'Failed to load Cog: {e}')
            raise
        return

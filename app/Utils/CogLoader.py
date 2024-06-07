import os


class CogLoader:
    """
    CogLoader: Loads Cogs for a bot from a directory.
    Raises error if directory doesn't exist or is empty (excluding __init__.py).
    """
    @staticmethod
    def load_cogs(bot, cogs_dir):
        if not os.path.exists(cogs_dir):
            raise FileNotFoundError(f'Error: Cogs directory not found: {cogs_dir}')

        try:
            for filename in os.listdir(cogs_dir):
                if filename.endswith('.py') and filename != '__init__.py':
                    bot.load_extension(f'app.Cogs.{filename[:-3]}')
                    print(f'Loaded {filename[:-3]}')
        except Exception as e:
            print(f'Failed to load Cog: {e}')
            raise

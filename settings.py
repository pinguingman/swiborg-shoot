class Settings():
    """store all settings for Game"""

    def __init__(self):
        """initialisation of game settings"""
        #screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_size = (1200, 800)
        self.bg_color = (0, 204 , 204)
        #ship parameters
        self.ship_size = (100, 100)
        self.ship_speed = 1
        self.ship_hp = 10000
        #file location
        self.image_path = 'images/'
        self.hero_path = 'hero2.png'
        self.hero_full_path = self.image_path + self.hero_path
        self.enemy_path = 'enemy.png'
        self.enemy_damaged_path = 'enemy_damaged.png'
        self.enemy_full_path = self.image_path + self.enemy_path
        self.enemy_damaged_full_path = self.image_path + self.enemy_damaged_path
        self.file_prefix = '~'
        #bullet settings
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = (33, 33, 0)
        self.bullet_speed = 1
        self.bullet_power = 20
        #level design
        self.lvl_number = 0
        self.lvl = { 'enemy_number' : [5, 10, 3, 1], 'enemy_type' : ['normal', 'fast', 'fat', 'boss'] }
        #enemy settings
        self.enemy_speed = 0.5
        self.enemy_size = (55, 72)
        self.enemy_hp = 100
        self.damage_frame_time = 10
        self.enemy_damage = 1
        #interface settings
        self.hp_barh = 30
        self.hp_color = (255, 0, 0)

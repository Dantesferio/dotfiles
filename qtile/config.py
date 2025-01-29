######################################### imports ######################################### 
from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os

######################################### color schemes ######################################### 
color = {
    "one dark": {
        "black"        : "#0C0E14",
        "white"        : "#ABB2BF",
        "orange"       : "#ed955a",
        "light-red"    : "#E06C75",
        "dark-red"     : "#b83e48",
        "green"        : "#98C379",
        "light-yellow" : "#E5C07B",
        "dark-yellow"  : "#D19A66",
        "blue"         : "#61AfEf",
        "magenta"      : "#C678DD",
        "purple"       : "#9d7cd8",
        "cyan"         : "#56B6C2",
        "gutter-gray"  : "#4B5263",
        "comment-gray" : "#5C6370"
    },
    "tokyo_night": {
        "black"        : "#1f2335",
        "white"        : "#ABB2BF",
        "orange"       : "#ff7519",
        "light-red"    : "#ff757f",
        "dark-red"     : "#c53b53",
        "green"        : "#c3e88d",
        "light-yellow" : "#ffc777",
        "dark-yellow"  : "#c98f3c",
        "blue"         : "#3d59a1",
        "magenta"      : "#ff007c",
        "purple"       : "#9d7cd8",
        "cyan"         : "#41a6b5",
        "gutter-gray"  : "#737aa2",
        "comment-gray" : "#545c7e"

    }
}

######################################### settings ######################################### 
mod = "mod4"
terminal = "alacritty"
cs = "one dark" # color scheme
group_list = "一 二 三 四 五 六 七".split(" ")
defalut_font_size = 14
defalut_icon_size = 27
defalut_bar_size = 27
focused_border_color = color[cs]["purple"]
unfocused_border_color = color[cs]["blue"]
#group_list = "1 2 3 4 5".split(" ")


######################################### key bindings ######################################### 
# A list of available commands that can be bound to keys can be found
# at https://docs.qtile.org/en/latest/manual/config/lazy.html
keys = [
    # change the focus: mod + arrow_keys
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),

    # change the focus to next window in Stack: mod + space
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # move the focused window in the current group: mod + shift + arrow_keys
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),

    # resize the focused window: mod + control + arrow_keys
    # reset the window sizes: mod + n
    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # toggle the focused window into floating layouts: mod + shift + space
    Key([mod, "shift"],"space", lazy.window.toggle_floating(), desc="toggle between floating and non-floating layouts"),
    
    # kill the focused window: mod + shift + q
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    
    # reload the qtile to apply config changes: mod + control + r
    Key([mod, "control"], "r", lazy.restart(), desc="Reload the config"),
    
    # toggle between layouts: mod + Tab:
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    
    # application launchers
    Key([mod, "shift"], "return", lazy.spawn("rofi -show drun -show-icons"), desc="dmenu application launcher",),
    Key([mod, "control"], "return", lazy.spawn("rofi -show run -show-icons"), desc="rofi command launcher",),
    
    # luanching apps
    Key([mod], "return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "n", lazy.spawn(f"{terminal} -e nvim"), desc="nvim editor"),
    Key([mod, "shift"], "e", lazy.spawn("thunar"), desc="thunar file manager"),
    Key([mod, "shift"], "f", lazy.spawn("firefox"), desc="firefox web browser"),
    Key([mod, "shift"], "a", lazy.spawn("audacious"), desc="audacious music player"),
    Key([mod, "shift"], "s", lazy.spawn("xfce4-screenshooter --region"), desc="launch a region screenshoot"),
    Key([mod, "shift"], "h", lazy.spawn("alacritty -e sudo /home/rebin/hid"), desc="hiddift VPN"),
    
    # opening the config file
    Key([mod, "shift"], "c", lazy.spawn("code /home/rebin/.config/qtile/config.py"), desc="open the config file in nvim"),

    # FN keys
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5"), desc="increase backlight level by 5%"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5"), desc="decrease backlight level by 5%"),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D default set Master 1+ toggle"), desc="mute the sound"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D default -M set Master 5%+"), desc="increase audio level by 5%"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D default -M set Master 5%-"), desc="decrease audio level by 5%"),


    # a simple power menu using dmenu
    Key([mod, "control"], "q", 
        lazy.run_extension(extension.CommandSet(
                commands={
                "shutdown": "poweroff",
                "reboot": "reboot",
                "sleep": "systemctl suspend",
                "log-out": "qtile cmd-obj -o cmd -f shutdown"
                },
                foreground="#ffffff",                
                dmenu_font="Ubuntu Bold",
                fontsize=defalut_font_size,
                selected_background=color[cs]["purple"]
            )
        )
    ),

    Key([mod, "control"], "p", 
        lazy.run_extension(extension.CommandSet(
                commands={
                    "Balanced": "powerprofilesctl set balanced",
                    "power-saver": "powerprofilesctl set power-saver",
                    "performance": "powerprofilesctl set performance",
                },
                foreground="#ffffff",                
                dmenu_font="Ubuntu Bold",
                fontsize=defalut_font_size,
                selected_background=color[cs]["purple"]
            )
        )
    ),
]



######################################### workspaces (groups) ######################################### 
# defining the groups using the names we declare at setting
groups = [Group(i) for i in group_list]

# we use mod+group_number or mod+shift+group_number to interact with groups
# so we need to assign a number to each group an then use that number to generate keybindings
group_keys = {}
num = 1
for i in group_list:
    group_keys[i] = str(num)
    num += 1

# now, group_keys dictionary contains groups and there coresponding number
# here we do generate the keybindings
for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                group_keys[i.name],
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                group_keys[i.name],
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )



######################################### layouts ######################################### 
layouts = [
    layout.MonadTall(
        border_width=2,
        margin=5,
        border_focus=focused_border_color,
        border_normal=unfocused_border_color
    ),

    layout.Max(),
    
    layout.Columns(
        border_width=2,
        margin=5,
        border_focus=focused_border_color,
        border_normal=unfocused_border_color
    ),
    
    # layout.Stack(num_stacks=2),
    
    # layout.Bsp(),
    
    layout.Matrix(
        border_width=2,
        margin=5,
        border_focus=focused_border_color,
        border_normal=unfocused_border_color
    ),
    
    #    layout.MonadWide(
    #    border_width=2,
    #    margin=10,
    #    border_focus=color[cs]["magenta"],
    #    border_normal=color[cs]["blue"]
    #),
    
    layout.RatioTile(
        border_width=2,
        margin=5,
        border_focus=focused_border_color,
        border_normal=unfocused_border_color
    ),
    
    # layout.Tile(),
    
    # layout.TreeTab(),
    
    layout.VerticalTile(
        border_width=2,
        margin=5,
        border_focus=focused_border_color,
        border_normal=unfocused_border_color
    ),
    
    # layout.Zoomy(),
]


######################################### bar and widgets ######################################### 
screens = [
    Screen(
        top=bar.Bar(
            [
                # ------------------------------ left ------------------------------
                widget.CurrentLayoutIcon(
                    font = "Ubuntu Bold", 
                    fontsize=defalut_font_size,
                    background=color[cs]["black"]
                ),

                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),

                widget.CPU(
                    format="CPU: {load_percent}%",
                    font = "Ubuntu Bold", 
                    fontsize=defalut_font_size,
                    background=color[cs]["black"],
                    foreground=color[cs]["purple"],
                ),

                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),

               
                widget.ThermalSensor(
                    font = "Ubuntu Bold", 
                    fontsize=defalut_font_size,
                    background=color[cs]["black"],
                    foreground=color[cs]["magenta"],
                    foreground_alert=color[cs]["light-red"],
                    tag_sensor="Package id 0",
                    fmt="TEMP: {}"
                ),

                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),

                widget.Memory(
                    format="MEM: {MemUsed: .2f} {mm}", 
                    measure_mem='G',
                    font = "Ubuntu Bold", 
                    fontsize=defalut_font_size,
                    background=color[cs]["black"],
                    foreground=color[cs]["blue"]
                ),

                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),

                widget.Battery(
                    font = "Ubuntu Bold", 
                    fontsize=defalut_font_size,
                    background=color[cs]["black"],
                    foreground=color[cs]["cyan"],
                    format="Battery: {char} {percent:2.0%}"
                ),

                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),

                widget.Backlight(
                    font = "Ubuntu Bold", 
                    fontsize=defalut_font_size,
                    background=color[cs]["black"],
                    foreground=color[cs]["green"],
                    backlight_name="intel_backlight",
                    format="BRT: {percent:2.0%}",
                    step=5
                ),

                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),
                # ------------------------------ center ------------------------------


                widget.Spacer(
                    background=color[cs]["black"]
                ),

                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),

                widget.GroupBox(
                    font = "Ubuntu Bold", 
                    fontsize=20,
                    disable_drag=True,
                    background=color[cs]["black"],
                    inactive=color[cs]["gutter-gray"],
                    block_highlight_text_color=color[cs]["purple"],
                    border_width=0,
                    highlight_method="line",
                    highlight_color=color[cs]["black"],
                    rounded=True
                ),
                
                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),

                widget.Spacer(
                    background=color[cs]["black"]
                ),

                # ------------------------------ right ------------------------------
                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),

                widget.GenPollCommand(
                    shell=True,
                    cmd="powerprofilesctl get",
                    fmt="Power: {}",
                    update_interval=5,
                    font = "Ubuntu Bold", 
                    fontsize=defalut_font_size,
                    background=color[cs]["black"],
                    foreground=color[cs]["green"],
                ),
                
                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),

                widget.GenPollCommand(
                    shell=True,
                    cmd="checkupdates | wc -l",
                    fmt="Updates: {}",
                    update_interval=900,
                    font = "Ubuntu Bold", 
                    fontsize=defalut_font_size,
                    background=color[cs]["black"],
                    foreground=color[cs]["cyan"],
                ),

                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),


                widget.Volume(
                    fmt="VOL: {}",
                    #emoji=True,
                    #emoji_list=["󰸈", "󰕿", "󰖀", "󰕾"],
                    font = "Ubuntu Bold",
                    padding=5,
                    fontsize=defalut_font_size,
                    foreground=color[cs]["blue"],
                    background=color[cs]["black"],
                    mute_command=['amixer','-q','set','Master','toggle']
                ),

                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),

                widget.Clock(
                    format="%A %d %b", 
                    font = "Ubuntu Bold", 
                    fontsize=defalut_font_size,
                    background=color[cs]["black"],
                    foreground=color[cs]["magenta"]
                ),

                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),

                widget.Clock(
                    format="%I:%M %p", 
                    font = "Ubuntu Bold", 
                    fontsize=defalut_font_size,
                    background=color[cs]["black"],
                    foreground=color[cs]["purple"]
                ),
                widget.Sep(
                    background=color[cs]["black"],
                    foreground=color[cs]["gutter-gray"]
                ),

                widget.Systray(
                    background=color[cs]["black"]
                ),

            ],
            defalut_bar_size,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=color[cs]["purple"],
    border_normal=color[cs]["blue"],
    border_width=2
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


# application startups:

@hook.subscribe.startup_complete
def startup():
    os.system(f"bash /home/{os.getlogin()}/.config/qtile/autostart.sh")

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

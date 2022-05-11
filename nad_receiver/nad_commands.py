"""
Commands and operators used by NAD.

CMDS[domain][function]
"""

from typing import Dict, Iterable, Union

CMDS: Dict[str, Dict[str, Dict[str, Union[str, Iterable[str]]]]] = {
    'main':
        {
            'dimmer':
                {'cmd': 'Main.Dimmer',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'lcd_darkmode':
                {'cmd': 'Main.LCD.DarkMode',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'lcd_display':
                {'cmd': 'Main.LCD.Display',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'lcd_frontview_bluos':
                {'cmd': 'Main.LCD.FrontView.BluOS',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'lcd_frontview_other':
                {'cmd': 'Main.LCD.FrontView.Other',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'lcd_brightness':
                {'cmd': 'Main.Brightness',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'mute':
                {'cmd': 'Main.Mute',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'power':
                {'cmd': 'Main.Power',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'subwoofer':
                {'cmd': 'Main.Speaker.Sub',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'enhanced_bass':
                {'cmd': 'Main.EnhancedBass',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'trim_center':
                {'cmd': 'Main.Trim.Center',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'trim_sub':
                {'cmd': 'Main.Trim.Sub',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'trim_surround':
                {'cmd': 'Main.Trim.Surround',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'video_resolution':
                {'cmd': 'Main.Video.Resolution',
                 'supported_operators': ['?']
                 },
            'video_hdr':
                {'cmd': 'Main.Video.HDR',
                 'supported_operators': ['?']
                 },
            'video_color':
                {'cmd': 'Main.Video.Color',
                 'supported_operators': ['?']
                 },
            'video_bits':
                {'cmd': 'Main.Video.Bits',
                 'supported_operators': ['?']
                 },
            'video_videomode':
                {'cmd': 'Main.VideoMode',
                 'supported_operators': ['?']
                 },
            'audio_codec':
                {'cmd': 'Main.Audio.Codec',
                 'supported_operators': ['?']
                 },
            'audio_channels':
                {'cmd': 'Main.Audio.Channels',
                 'supported_operators': ['?']
                 },
            'audio_rate':
                {'cmd': 'Main.Audio.Rate',
                 'supported_operators': ['?']
                 },
            'temp_back':
                {'cmd': 'Main.Temp.Back',
                 'supported_operators': ['?']
                 },
            'temp_center':
                {'cmd': 'Main.Temp.Center',
                 'supported_operators': ['?']
                 },
            'temp_front':
                {'cmd': 'Main.Temp.Front',
                 'supported_operators': ['?']
                 },
            'temp_height':
                {'cmd': 'Main.Temp.Height',
                 'supported_operators': ['?']
                 },
            'temp_psu':
                {'cmd': 'Main.Temp.PSU',
                 'supported_operators': ['?']
                 },
            'temp_surround':
                {'cmd': 'Main.Temp.Surround',
                 'supported_operators': ['?']
                 },
            'fan_actual':
                {'cmd': 'Internal.Fan.Actual',
                 'supported_operators': ['?']
                 },
            'fan_requested':
                {'cmd': 'Internal.Fan.Requested',
                 'supported_operators': ['?']
                 },
            'fan_status':
                {'cmd': 'Internal.Fan.Status',
                 'supported_operators': ['?']
                 },
            'speaker_front_config':
                {'cmd': 'Main.Speaker.Front.Config',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'speaker_center_config':
                {'cmd': 'Main.Speaker.Center.Config',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'speaker_surround_config':
                {'cmd': 'Main.Speaker.Surround.Config',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'speaker_front_frequency':
                {'cmd': 'Main.Speaker.Front.Frequency',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'speaker_center_frequency':
                {'cmd': 'Main.Speaker.Center.Frequency',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'speaker_surround_frequency':
                {'cmd': 'Main.Speaker.Surround.Frequency',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'cec_arc':
                {'cmd': 'Main.CEC.Arc',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'cec_audio':
                {'cmd': 'Main.CEC.Audio',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'cec_power':
                {'cmd': 'Main.CEC.Power',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'cec_switch':
                {'cmd': 'Main.CEC.Switch',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'volume':
                {'cmd': 'Main.Volume',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'ir':
                {'cmd': 'Main.IR',
                 'supported_operators': ['=']
                 },
            'listeningmode':
                {'cmd': 'Main.ListeningMode',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'version':
                {'cmd': 'Main.Version',
                 'supported_operators': ['?']
                 },
            'speaker_a':
                {'cmd': 'Main.SpeakerA',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'speaker_b':
                {'cmd': 'Main.SpeakerB',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'tape_monitor':
                {'cmd': 'Main.Tape1',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'auto_standby':
                {'cmd': 'Main.AutoStandby',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'sleep':
                {'cmd': 'Main.Sleep',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'source':
                {'cmd': 'Main.Source',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'model':
                {'cmd': 'Main.Model',
                 'supported_operators': ['?']
                 },
        },
    'tuner':
        {
            'am_frequency':
                {'cmd': 'Tuner.AM.Frequency',
                 'supported_operators': ['+', '-']
                 },
            'am_preset':
                {'cmd': 'Tuner.AM.Preset',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'band':
                {'cmd': 'Tuner.Band',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'fm_frequency':
                {'cmd': 'Tuner.FM.Frequency',
                 'supported_operators': ['+', '-']
                 },
            'fm_mute':
                {'cmd': 'Tuner.FM.Mute',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'fm_preset':
                {'cmd': 'Tuner.FM.Preset',
                 'supported_operators': ['+', '-', '=', '?']
                 }
        }
}

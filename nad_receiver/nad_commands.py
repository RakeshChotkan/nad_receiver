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
            'info':
                {'cmd': '',
                 'supported_operators': ['?']
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
            'sleep':
                {'cmd': 'Main.Sleep',
                 'supported_operators': ['+', '-']
                 },
            'source':
                {'cmd': 'Main.Source',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'version':
                {'cmd': 'Main.Version',
                 'supported_operators': ['?']
                 },
            'speaker_a':
                {'cmd': 'Main.SpeakerA',
                 'supported_operators': ['+', '-', '=', '?'],
                 },
            'speaker_b':
                {'cmd': 'Main.SpeakerB',
                 'supported_operators': ['+', '-', '=', '?'],
                 },
            'tape_monitor':
                {'cmd': 'Main.Tape1',
                 'supported_operators': ['+', '-', '=', '?'],
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

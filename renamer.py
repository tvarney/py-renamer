
import os
import os.path
import tkinter

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Optional


def rename_regexp(path: str, pattern_original: str, pattern_new: str) -> int:
    return 0


def rename_normal(path: str, pattern_original: str, pattern_new: str) -> int:
    renamed = 0
    for file_name in os.listdir(path):
        new_file_name = file_name.replace(pattern_original, pattern_new)
        if new_file_name != file_name:
            renamed += 1
            os.rename(os.path.join(path, file_name), os.path.join(path, new_file_name))
    return renamed


def rename(path: str, pattern_original: str, pattern_new: str, use_regexp: bool = False) -> int:
    if use_regexp:
        return rename_regexp(path, pattern_original, pattern_new)
    return rename_normal(path, pattern_original, pattern_new)


class Application(object):
    def __init__(self):
        self._tk = None  # type: Optional[tkinter.Tk]
        self._txtPath = None  # type: Optional[tkinter.Entry]
        self._txtPatternOriginal = None  # type: Optional[tkinter.Entry]
        self._txtPatternNew = None  # type: Optional[tkinter.Entry]

    def run(self) -> int:
        self._create_gui()
        self._tk.mainloop()
        return 0

    def _create_gui(self):
        pass

    def _callback_apply(self):
        pass

    def _callback_browse(self):
        pass


if __name__ == "__main__":
    import sys
    app = Application()
    sys.exit(app.run())

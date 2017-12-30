
import os
import os.path
import tkinter
import tkinter.filedialog

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
        self._destroy_gui()
        return 0

    def _create_gui(self):
        self._tk = tkinter.Tk()
        frm_row_1 = tkinter.Frame(self._tk)
        lbl_path = tkinter.Label(frm_row_1, text="Path:")
        self._txtPath = tkinter.Entry(frm_row_1)
        btn_browse = tkinter.Button(frm_row_1, text="...", command=self._callback_browse)
        lbl_path.pack(side=tkinter.LEFT)
        self._txtPath.pack(side=tkinter.LEFT, fill=tkinter.X, expand=1)
        btn_browse.pack(side=tkinter.LEFT)

        frm_row_2 = tkinter.Frame(self._tk)
        lbl_original = tkinter.Label(frm_row_2, text="Replace:")
        self._txtPatternOriginal = tkinter.Entry(frm_row_2)
        lbl_with = tkinter.Label(frm_row_2, text="With:")
        self._txtPatternNew = tkinter.Entry(frm_row_2)
        lbl_original.pack(side=tkinter.LEFT)
        self._txtPatternOriginal.pack(side=tkinter.LEFT, fill=tkinter.X, expand=1)
        lbl_with.pack(side=tkinter.LEFT)
        self._txtPatternNew.pack(side=tkinter.LEFT, fill=tkinter.X, expand=1)

        frm_row_3 = tkinter.Frame(self._tk)
        btn_apply = tkinter.Button(frm_row_3, text="Apply", command=self._callback_apply)
        btn_apply.pack(side=tkinter.RIGHT)

        frm_row_1.pack(side=tkinter.TOP, fill=tkinter.X, expand=1)
        frm_row_2.pack(side=tkinter.TOP, fill=tkinter.X, expand=1)
        frm_row_3.pack(side=tkinter.TOP, fill=tkinter.X, expand=1)

    def _destroy_gui(self):
        # TODO: Destroy the tkinter instance and GUI here
        pass

    def _callback_apply(self):
        directory = self._txtPath.get()
        pattern_original = self._txtPatternOriginal.get()
        pattern_new = self._txtPatternNew.get()
        # TODO: Convert error messages here to use a pop-up box
        if not os.path.exists(directory):
            print("Directory does not exist")
            return
        if not os.path.isdir(directory):
            print("Given path is not a directory")
            return
        if pattern_original == "":
            print("No pattern to match")
            return
        # TODO: Display a message box or something to indicate how many files were renamed
        # TODO: Add option for regexp matching of file names
        rename(directory, pattern_original, pattern_new, False)

    def _callback_browse(self):
        directory = tkinter.filedialog.askdirectory()
        if directory != "":
            self._txtPath.delete(0, tkinter.END)
            self._txtPath.insert(0, directory)


if __name__ == "__main__":
    import sys
    app = Application()
    sys.exit(app.run())

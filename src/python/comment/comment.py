# -*- coding:utf-8 -*_
"""
===========================
``comment`` Comment Example
===========================

See Also
--------

References
----------
.. [1] source code comment in numpy, http://www.numpy.org/

Examples
--------
Module comment: like this, contains sections: title, See Also, References, Examples

"""


class Comment(object):
    """
    Short description for calss comment.

    Detail description for class comment.
    """

    def __init__(self, *args):
        """
        Short description for this method, sometimes ignore.

        Detail description for the method, sometimes ignore.

        Parameters
        ----------
        args: some description about this argument, if no argument, no this section.

        Returns
        -------
        return-variable-name: some description

        Raises
        ------
        ExceptionClassName: some description, always condition description

        Notes
        -----
        Something need to note.

        Examples
        --------
        Show some usage examples here if you want.
        """
        # here is some comments in-line
        if args:
            pass

def func_comment():
    """
    Same as comments for class's method
    """
    pass


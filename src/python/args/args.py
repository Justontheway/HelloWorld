# -*- coding:utf-8 -*-


import sys
import argparse


def git_clone(args):
    print('in git_clone')
    print(args)

def git_init(args):
    print('in git_init')
    print(args)

def git_commit(args):
    print('in git_commit')
    print(args)

def subcommands(args):
    """
    # 1.1 add long option with arg
    parser.add('--arg', type=int, help='long option with arg')
    # 1.2 add long option without arg (True,False)
    parser.add('--bool', action='store_true', help='long option without arg (true-false)')
    # 1.3 add long option without arg (Count)
    parser.add('--count', action='count', help='long option without arg (count)')

    # 2.1 add short option with arg
    parser.add('-a', type=int, help='short option with arg')
    # 2.2 add short option without arg (True,False)
    parser.add('-b', action='store_true', help='short option without arg (true-false)')
    # 2.3 add short option without arg (Count)
    parser.add('-c', action='count', help='short option without arg (count)')

    # 3.1 add long short option with arg
    parser.add('-q', '--quiet', type=int, help='long short option with arg')
    # 3.2 add long short option without arg (True,False)
    parser.add('-v', '--verbosity', action='store_true', help='long short option without arg (true-false)')
    # 3.3 add long short option without arg (Count)
    parser.add('-t', '--times', action='count', help='long short option without arg (count)')

    # 4.1 add mutually exclusive option without arg
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    # add_argument_group
    """
    main_parser_usage = """git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]"""
    main_parser_epilog = """git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept."""

    clone_parser_usage = """usage: git clone [<options>] [--] <repo> [<dir>]"""
    clone_parser_epilog = ""

    init_parser_usage = """usage: git init [-q | --quiet] [--bare] [--template=<template-directory>] [--shared[=<permissions>]] [<directory>]"""
    init_parser_epilog = ""

    commit_parser_usage = "usage: git commit [<options>] [--] <pathspec>..."
    commit_parser_epilog = ""
    # CREATE TOP-LEVEL PARSER
    #Keyword Arguments:
    #- prog - The name of the program (default: sys.argv[0])
    #- usage - The string describing the program usage (default: generated from arguments added to parser)
    #- description - Text to display before the argument help (default: none)
    #- epilog - Text to display after the argument help (default: none)
    #- parents - A list of ArgumentParser objects whose arguments should also be included
    #- formatter_class - A class for customizing the help output
    #- prefix_chars - The set of characters that prefix optional arguments (default: ‘-‘)
    #- fromfile_prefix_chars - The set of characters that prefix files from which additional arguments should be read (default: None)
    #    additional arguments
    #- argument_default - The global default value for arguments (default: None)
    #- conflict_handler - The strategy for resolving conflicting optionals (usually unnecessary)
    #- add_help - Add a -h/--help option to the parser (default: True)
    #- allow_abbrev - Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)
    parser = argparse.ArgumentParser(prog='git', usage=main_parser_usage, description=None,
        epilog=main_parser_epilog)

    # CREATE SUB-COMMANDS
    #ArgumentParser.add_subparsers([title ][, description ][, prog ][, parser_class ][, action ]
    #    [, option_string ][, dest ][, help ][, metavar ])
    #Keyword Arguments:
    #- title - title for the sub-parser group in help output; by default “subcommands” if description is provided, otherwise uses title for positional arguments
    #- description - description for the sub-parser group in help output, by default None
    #- prog - usage information that will be displayed with sub-command help, by default the name of the program and any positional arguments before the subparser argument
    #- parser_class - class which will be used to create sub-parser instances, by default the class of the current parser (e.g. ArgumentParser)
    #- action - the basic type of action to be taken when this argument is encountered at the command line
    #- dest - name of the attribute under which sub-command name will be stored; by default None and no value is stored
    #- help - help for sub-parser group in help output, by default None
    #- metavar - string presenting available sub-commands in help; by default it is None and presents sub-commands in form {cmd1, cmd2, ..}
    subparsers = parser.add_subparsers(dest='subcmd', title='These are common Git commands used in various situations',
            description=None, metavar='')

    # create the parser for the 'clone' command
    parser_clone = subparsers.add_parser('clone', prog='git clone', help='Clone a repository into a new directory',
            usage=clone_parser_usage, epilog=clone_parser_epilog)
    parser_clone.set_defaults(func=git_clone)
    parser_clone.add_argument('bar', type=int, help='bar help')

    # create the parser for the 'init' command
    parser_init = subparsers.add_parser('init', prog='git init', help='Create an empty Git repository or reinitialize an existing one',
            usage=init_parser_usage, epilog=init_parser_epilog)
    parser_init.set_defaults(func=git_init)
    parser_init.add_argument('--template', metavar='<template-directory>', help='directory from which templates will be used')
    parser_init.add_argument('--bare', action='store_true', help='create a bare repository')
    parser_init.add_argument('--shared', metavar='[=<permissions>]', help='specify that the git repository is to be shared amongst several users')
    parser_init.add_argument('-q', '--quiet', action='store_true', help='be quiet')
    parser_init.add_argument('--separate-git-dir', metavar='<gitdir>', help='separate git dir from working tree')
    #ArgumentParser.set_defaults(**kwargs)

    # create the parser for the 'commit' command
    #parser_commit = subparsers.add_parser('commit', aliases=['ci'], prog='git commit', help='Record changes to the repository',
    parser_commit = subparsers.add_parser('commit', prog='git commit', help='Record changes to the repository',
            usage=commit_parser_usage, epilog=commit_parser_epilog)
    parser_init.set_defaults(func=git_commit)
    parser_commit.add_argument('-q', '--quiet', action='store_true', help='suppress summary after successful commit')
    parser_commit.add_argument('-v', '--verbose', action='store_true', help='show diff in commit message template')
    #ArgumentParser.add_argument_group(title=None, description=None)
    group_commit_msg = parser_commit.add_argument_group(title='Commit message options', description=None)
    group_commit_msg.add_argument('-F', '--file', metavar='<file>', help='read message from file')
    group_commit_msg.add_argument('--author', metavar='<author>', help='override author for commit')
    group_commit_msg.add_argument('--date', metavar='<date>', help='override date for commit')
    group_commit_msg.add_argument('-m', '--message', metavar='<message>', help='commit message')
    group_commit_msg.add_argument('-c', '--reedit-message', metavar='<commit>', help='reuse and edit message from specified commit')
    group_commit_msg.add_argument('-C', '--reuse-message', metavar='<commit>', help='reuse message from specified commit')
    group_commit_msg.add_argument('--fixup', metavar='<commit>', help='use autosquash formatted message to fixup specified commit')
    group_commit_msg.add_argument('--squash', metavar='<commit>', help='use autosquash formatted message to squash specified commit')
    group_commit_msg.add_argument('--reset-author', metavar='<commit>', help='the commit is authored by me now (used with -C/-c/--amend)')
    group_commit_msg.add_argument('-s', '--signoff', action='store_true', help='add Signed-off-by:')
    group_commit_msg.add_argument('-t', '--template', metavar='<file>', help='use specified template file')
    group_commit_msg.add_argument('-e', '--edit', action='store_true', help='force edit of commit')
    group_commit_msg.add_argument('--cleanup', metavar='<default>', help='how to strip spaces and #comments from message')
    group_commit_msg.add_argument('--status', action='store_true', help='include status in commit message template')
    group_commit_msg.add_argument('-S', '--gpg-sign', metavar='[=<key-id>]', help='GPG sign commit')

    group_commit_ctx = parser_commit.add_argument_group(title='Commit contents options', description=None)
    group_commit_ctx.add_argument('-a', '--all', action='store_true', help='commit all changed files')
    group_commit_ctx.add_argument('-i', '--include', action='store_true', help='add specified files to index for commit')
    group_commit_ctx.add_argument('--interactive', action='store_true', help='interactively add files')
    group_commit_ctx.add_argument('-p', '--patch', action='store_true', help='interactively add changes')
    group_commit_ctx.add_argument('-o', '--only', action='store_true', help='commit only specified files')
    group_commit_ctx.add_argument('-n', '--no-verify', action='store_true', help='bypass pre-commit and commit-msg hooks')
    group_commit_ctx.add_argument('--dry-run', action='store_true', help='show what would be committed')
    group_commit_ctx.add_argument('--short', action='store_true', help='show status concisely')
    group_commit_ctx.add_argument('--branch', action='store_true', help='show branch information')
    group_commit_ctx.add_argument('--ahead-behind', action='store_true', help='compute full ahead/behind values')
    group_commit_ctx.add_argument('--porcelain', action='store_true', help='machine-readable output')
    group_commit_ctx.add_argument('--long', action='store_true', help='show status in long format (default)')
    group_commit_ctx.add_argument('-z', '--null', action='store_true', help='terminate entries with NUL')
    group_commit_ctx.add_argument('--amend', action='store_true', help='amend previous commit')
    group_commit_ctx.add_argument('--no-post-rewrite', action='store_true', help='bypass post-rewrite hook')
    group_commit_ctx.add_argument('-u', '--untracked-files', metavar='[=<mode>]', choices=['all', 'normal', 'no'], help='show untracked files, optional modes: all, normal, no. (Default: all)')

    # ADD ARGUMENT
    #ArgumentParser.add_argument(name or  ags...[, action ][, nargs ][, const ][, default ][, type ]
    #    [, choices ][, required ][, help ][, metavar ][, dest ])
    #- name or ags - Either a name or a list of option strings, e.g. foo or -f, --foo.
    #- action - The basic type of action to be taken when this argument is encountered at the command line.
    #    store, store_const, store_true, store_false, append, append_const, count, help, version,
    #    subclass of Action with methods __call__ | __init__ override.
    #- nargs - The number of command-line arguments that should be consumed.
    #- const - A constant value required by some action and nargs selections.
    #- default - The value produced if the argument is absent from the command line.
    #- type - The type to which the command-line argument should be converted, built-in types and functions.
    #- choices - A container of the allowable values for the argument.
    #- required - Whether or not the command-line option may be omitted (optionals only).
    #- help - A brief description of what the argument does, %(prog)s, %(type)s, %(default)s.
    #- metavar - A name for the argument in usage messages.
    #- dest - The name of the attribute to be added to the object returned by parse_args().
    

    parser.add_argument('--version', dest='version', action='store_true', help='print version number', required=False)
    parser.add_argument('-C', dest='path', default='path', type=str, help='C help', required=False)
    parser.add_argument('-c', dest='conf', default='conf', type=str)#, help='C help', required=False)
    flags = parser.parse_args(args)
    flags.func(flags)


if __name__ == "__main__":
    subcommands(sys.argv[1:])


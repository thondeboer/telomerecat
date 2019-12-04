import sys
from .version import __version__

def add_input_telbam_arg(parser):
  parser.add_argument(
    "input", metavar="TELBAM(S)", nargs="+", help="The TELBAM(s) that we wish to analyse"
  )


def add_input_bam_arg(parser):
  parser.add_argument(
    "input",
    metavar="BAM(S)",
    nargs="+",
    help=("BAM file(s) for which we wish to\n" "generate telomere length estimates"),
  )


def add_trim_arg(parser):
  parser.add_argument(
    "-t",
    "--trim",
    type=int,
    metavar="INT",
    default=0,
    help="Use only the amount of sequence specified by this  \n"
    "option (i.e if the value 90 is supplied\n"
    "then only the first 90 bases are\n"
    "considered) [Default: Whole read]",
  )


def add_outbam_dir_arg(parser):
  parser.add_argument(
    "--outbam_dir",
    metavar="DIR",
    type=str,
    default=None,
    help=(
      "Output folder for bams which have all reads with at least 2 occurences\n"
      "of the telomeric hexamer. [Default: None, telbams will be discarded]"
    ),
  )


def add_output_csv_arg(parser):
  parser.add_argument(
    "--output",
    metavar="PATH",
    type=str,
    default="./telomerecat_length.csv",
    help=(
      "Specify output path for length estimation CSV.\n"
      "[Default: './telomerecat_length.csv']"
    ),
  )


def add_nreads_for_each_task_arg(parser):
  parser.add_argument(
    "-s",
    type=int,
    metavar="INT",
    default=250000,
    help=("The amount of reads considered by each\n" "distributed task. [Default: 250000]"),
  )

add_arg = {
  'input_telbam': add_input_telbam_arg,
  'input_bam': add_input_bam_arg,
  'trim': add_trim_arg,
  'outbam_dir': add_outbam_dir_arg,
  'output_csv': add_output_csv_arg,
  'nreads_for_task': add_nreads_for_each_task_arg
}

def exit_with_msg(message):
  sys.stderr.write(message)
  sys.stderr.flush()
  sys.exit(1)

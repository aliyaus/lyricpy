import time
import re 

# Function to parse time from the line
def parse_time_and_clean_line(line):

  # Extract timestamp inside brackets
  timestamp_pattern_regex = r'\[(.*?)\]'
  timestamp_pattern_matches = re.findall(timestamp_pattern_regex, line)

  # Extract remaining string after last bracket
  remaining = re.split(timestamp_pattern_regex, line)

  if timestamp_pattern_matches and remaining:
    return timestamp_pattern_matches[0], remaining[-1].strip()
  else:
    return None, None


def convert_mmssmmm_to_seconds(mmssmmm):
    mins, secs = map(float, mmssmmm.split(':'))
    return mins * 60 + secs


def split_string(s, chunk_size):
    return [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]
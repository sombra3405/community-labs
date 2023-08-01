#!/bin/sh

check_file_at_folder() {
  file_check="/ubuntu/$1"
  [ -f "${file_check}" ]
}

fail() {
  echo "fail"
  exit 1
}

success() {
  echo "success"
  exit 0
}

check_file_at_folder "hello.txt" || fail

success

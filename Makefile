# makefile for running tests

default: tests

.PHONY: tests shell-tests python-tests ruby-tests
.PHONY: unittests shell-unittests python-unittests ruby-unittests;

tests: shell-tests python-tests ruby-tests;

unittests: shell-unittests python-unittests ruby-unittests;

ACTDIRS := $(shell ls -d acts)

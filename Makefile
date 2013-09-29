# makefile for running tests
# can be called from jenkins
# todo: may need to set PATH appropriately

default: tests

.PHONY: tests shell-tests python-tests ruby-tests
.PHONY: unittests shell-unittests shiot-tests python-unittests ruby-unittests

tests:
	@$(MAKE) -k shell-tests shiot-tests python-tests ruby-tests

# make -k doesn't exit on first error
unittests:
	@$(MAKE) -k shell-unittests python-unittests ruby-unittests

shell-tests:
	@$(MAKE) -k shiot-tests shunit2-tests

python-tests:
	@$(MAKE) -k python-unittests

ruby-tests:
	@$(MAKE) -k ruby-unittests

BUILDROOT:=$(shell /bin/pwd -P)
ACT_BASE:=$(BUILDROOT)/acts
ACT_DIRS := $(shell ls -d $(ACT_BASE)/*)
TEST_REP_DIR=$(BUILDROOT)/test-reports
BIN=$(BUILDROOT)/bin

$(TEST_REP_DIR):
	mkdir -p $@

python-unittests: $(TEST_REP_DIR)
	cd $(ACT_BASE) \
	&& nosetests --with-xunit \
	--xunit-file=$(TEST_REP_DIR)/nosetests.xml

ruby-unittests: $(TEST_REP_DIR)
	cd $(ACT_BASE) \
	&& rspec -r rspec_junit_formatter --format RspecJunitFormatter \
	-o $(TEST_REP_DIR)/rspec.xml \

shunit2-tests:
	@echo '($@ not working yet)' && exit 1

shiot-tests: $(TEST_REP_DIR)
	cd $(ACT_BASE) \
	&& $(BIN)/shiot-xunit -v -o $(TEST_REP_DIR)/shiot.xml


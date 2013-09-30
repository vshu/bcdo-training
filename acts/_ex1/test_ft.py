def test():
	setup_test()
	try:
		do_test()
		make_test_assertions()
	finally:
		cleanup_after_test()

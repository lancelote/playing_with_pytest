def test_disabling_capturing(capsys):
    print('this output is captured')
    with capsys.disabled():
        print('output not captured, going directly to sys.stdout')
    print('this output is also captured')

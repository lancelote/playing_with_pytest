def test_create_file(tmpdir):
    hello = tmpdir.mkdir('sub').join('hello.txt')
    hello.write('content')
    assert hello.read() == 'content'
    assert len(tmpdir.listdir()) == 1

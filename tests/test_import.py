

def test_import_package():
    import bufflib
    bufflib.load_data
    bufflib.plotting
    bufflib.cluster

    # confirm that the module works
    bufflib.load_data.test = 1
    bufflib.plotting.test = 1
    bufflib.cluster.test = 1

    assert bufflib.load_data.test
    assert bufflib.plotting.test
    assert bufflib.cluster.test


def test_import_load_data():
    from bufflib import load_data
    load_data.test = 1
    assert load_data.test


def test_import_plotting():
    from bufflib import plotting
    plotting.test = 1
    assert plotting.test


def test_import_cluster():
    from bufflib import cluster
    cluster.test = 1
    assert cluster.test

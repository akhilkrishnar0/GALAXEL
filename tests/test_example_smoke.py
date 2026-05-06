from galaxy_flux_pipeline.io import read_targets

def test_example_targets_exist():
    df=read_targets('data/examples/targets_example.csv')
    assert {'UGC 9024','NGC 6902'}.issubset(set(df['galaxy_name']))

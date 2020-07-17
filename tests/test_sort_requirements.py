from click.testing import CliRunner

from claudio_requirements_sorter import cli

from claudio_requirements_sorter.sort_requirements import sort_requirements


def test_sort_requirements(requirements):
    unsorted_requirements = requirements["unsorted_requirements"]
    sorted_requirements = requirements["sorted_requirements"]

    new_requirements = sort_requirements(requirements=unsorted_requirements)
    assert sorted_requirements == new_requirements


def test_command_line_interface(requirements):
    """Test the CLI."""
    src = "unsorted_requirements.txt"
    dst = "sorted_requirements.txt"

    runner = CliRunner()
    with runner.isolated_filesystem():
        with open(src, "w") as f:
            f.write("\n".join(requirements["unsorted_requirements"]))

        result = runner.invoke(cli.main, [src, dst])
        assert result.exit_code == 0
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

        expected_requirements = requirements["sorted_requirements"]

        with open(dst) as f:
            actual_requirements = f.read().split()

        assert actual_requirements == expected_requirements

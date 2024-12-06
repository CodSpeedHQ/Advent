<div align="center">
  <img alt="Cover Image" src="./cover.png" width="100%">
  <sub>A performance challenge based on the Advent of Code problems</sub>
</div>

<br />

Learn more about Advent of CodSpeed and how to participate on the [Advent of CodSpeed page](https://codspeed.io/advent/).

> [!IMPORTANT]
> Only Rust solutions are supported for now. Python and Node.js are planned in the future since it's already supported by [CodSpeed](https://codspeed.io).

## Repository setup

You need to expose a library that exposes a module for each day. In each module, you need to expose a `part1` and a `part2` function that takes a `&str` and returns an `impl Display`.

More specifically, the following return types are allowed:

- Integer types (`i32`, `i64`, `u32`, `u64`, `usize`, `isize`, etc.)
- Floating-point types (`f32`, `f64`)
- Single character (`char`)
- String slice (`&str`) or `String`

For example, to solve part 2 of day 5, we'll call: `crate::day5::part2(input)`.

> [!NOTE]
> Day numbers are not zero-padded.

We follow the standard defined in [`cargo-aoc`](https://github.com/gobanos/cargo-aoc) for the project structure. See this [example repository](https://github.com/gobanos/advent-of-code-2015) for a reference.

## Adding your solutions to the leaderboard

Add your repository [here](https://github.com/CodSpeedHQ/Advent/issues/new?assignees=&labels=repo%2Cadd&projects=&template=new.yml&title=Add+%3Crepo_name%3E+).

## Testing your Rust solution

You can visit the [rust-runner](./rust-runner/) folder to test your Rust solution locally and make sure it will be picked up by the runner if you registered your repository.

## Support

Join us on [Discord](https://discord.gg/NDa4PBKWaa) if you need help or want to contribute.

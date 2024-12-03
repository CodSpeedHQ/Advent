# Advent of CodSpeed - Rust Runner

## Testing that your Rust solution will be picked up by the runner

1. Clone this repository
1. Add the following files in this directory:
   1. `input.txt` -> The input file for the day you want to test
   1. `output-1.txt` -> The expected output for part 1
   1. `output-2.txt` -> The expected output for part 2
1. Bind this runner to your solution:
   - For regular repositories, run:
     ```bash
     cargo add --git <YOUR_REPO_URL> --rename solution
     ```
   - If you specified a sub crate when you registered your solution, run:
     ```bash
     cargo add --git <YOUR_REPO_URL> <YOUR_CRATE_NAME> --rename solution
     ```
1. If you specified a toolchain while registering your solution, set it in the
   `rust-toolchain.toml` file:
   ```toml
   [toolchain]
   channel = "<YOUR TOOLCHAIN GOES HERE>"
   ```
1. Run the following command to set the day you want to test:
   ```bash
   export DAY_NUMBER=<day_number>
   ```
1. Install `cargo-codspeed`:
   ```bash
   cargo binstall cargo-codspeed
   ```
   (make sure you have `cargo-binstall` installed, if not, run `cargo install cargo-binstall`)
1. Build the benchmarks:
   ```bash
   cargo codspeed build
   ```
1. Run the benchmarks locally (without instrumentation):
   ```bash
   cargo codspeed run
   ```

If you don't see any errors, your solution is ready to be picked up by the runner and you will see the results on the leaderboard.

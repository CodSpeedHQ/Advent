use codspeed_criterion_compat::{criterion_group, criterion_main, Criterion};
use rust_runner::{check_result, Output};
use std::hint::black_box;

paste::paste! {
    use solution::[<day env!("DAY_NUMBER")>]::{part1};
}

fn bench_part1(c: &mut Criterion) {
    let mut g = c.benchmark_group(concat!("day", env!("DAY_NUMBER")));
    let input = include_str!("./input.txt");
    #[inline(never)]
    fn routine(input: &str) -> impl Output + '_ {
        part1(black_box(input))
    }
    g.bench_with_input("part1", input, |b, i| b.iter(|| routine(i)));
    let output = routine(input);
    let expected = include_str!("./output-1.txt");
    check_result(output, expected, 1);
}

criterion_group!(benches, bench_part1);
criterion_main!(benches);

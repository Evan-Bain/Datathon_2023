% begin: code to run "basic" method

first_num = 1;
second_num = 2;

output_of_sum = basic(first_num, second_num);
fprintf("basic output: %d\n", output_of_sum);

% end: code to run "basic" method

fprintf('\n');

% begin: code to run "multiple_operations" method
first_num = 4;
second_num = 8;
out_sum = 0;
out_diff = 0;
out_mult = 0;
out_div = 0;

[out_sum, out_diff, out_mult, out_div] = multiple_operations(first_num, second_num);
fprintf("multiple_operations output:\n");
fprintf("sum: %d\n", out_sum);
fprintf("difference: %d\n", out_diff);
fprintf("multiplication: %d\n", out_mult);
fprintf("division: %d\n", out_div);

% end: code to run "multiple_operations" method

fprintf('\n');
function FormSelect({
  label,
  name,
  value,
  onChange,
  options,
}) {
  return (
    <div>
      <label className="block text-sm font-semibold mb-2 text-gray-700">
        {label}
      </label>

      <select
        name={name}
        value={value}
        onChange={onChange}
        className="w-full rounded-lg border border-gray-300 p-3 focus:border-blue-600 focus:ring-2 focus:ring-blue-300 outline-none"
      >
        {options.map((option) => (
          <option key={option}>{option}</option>
        ))}
      </select>
    </div>
  );
}

export default FormSelect;
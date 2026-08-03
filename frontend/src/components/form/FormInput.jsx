function FormInput({
  label,
  name,
  value,
  onChange,
  type = "text",
}) {
  return (
    <div>
      <label className="block text-sm font-semibold mb-2 text-gray-700">
        {label}
      </label>

      <input
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        className="w-full rounded-lg border border-gray-300 p-3 focus:border-blue-600 focus:ring-2 focus:ring-blue-300 outline-none"
      />
    </div>
  );
}

export default FormInput;
export default function guardrail(mathFunction) {
  const queue = [];

  try {
    queue.push(mathFunction(mathFunction));
  } catch (error) {
    queue.push(error.toString());
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}

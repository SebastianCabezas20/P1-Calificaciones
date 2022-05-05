<template>
  <div class="flex flex-wrap bg-gray-100 w-full h-screen">
    <Sidebar> </Sidebar>

    <div class="w-5/6 ml-80">
      <Navbar> </Navbar>
      <section class="text-white bg-naranja-usach">
        <div class="max-w-screen-xl px-2 py-1 mx-auto sm:px-2 lg:px-0">
          <ul class="border border-white sm:grid sm:grid-cols-2 lg:grid-cols-3">
            <li class="p-8 border border-white">
              <p class="text-3xl font-extrabold">50</p>
              <p class="mt-1 text-xl font-medium">Cursos Disponibles</p>
            </li>

            <li class="p-8 border border-white">
              <p class="text-3xl font-extrabold">190k+</p>
              <p class="mt-1 text-xl font-medium">
                Cursos Que requieren atencion
              </p>
            </li>

            <li class="p-8 border border-white">
              <p class="text-3xl font-extrabold">$150k+</p>
              <p class="mt-1 text-xl font-medium">Cursos que no se</p>
            </li>

            <li class="p-8 border border-white">
              <p class="text-3xl font-extrabold">10</p>
              <p class="mt-1 text-xl font-medium">Apelaciones Totales</p>
            </li>

            <li class="p-8 border border-white">
              <p class="text-3xl font-extrabold">1</p>
              <p class="mt-1 text-xl font-medium">Apelaciones Pendientes</p>
            </li>

            <li class="p-8 border border-white">
              <p class="text-3xl font-extrabold">6</p>
              <p class="mt-1 text-xl font-medium">Apelaciones resueltas</p>
            </li>
          </ul>
        </div>
      </section>

      <div class="overflow-x-auto">
        <div
          class="overflow-hidden overflow-x-auto border border-gray-100 rounded"
        >
          <table class="min-w-full text-sm divide-y divide-gray-200">
            <thead>
              <tr class="bg-gray-50">
                <th
                  class="
                    px-4
                    py-2
                    font-medium
                    text-left text-gray-900
                    whitespace-nowrap
                  "
                >
                  Name
                </th>
                <th
                  class="
                    px-4
                    py-2
                    font-medium
                    text-left text-gray-900
                    whitespace-nowrap
                  "
                >
                  Date of Birth
                </th>
                <th
                  class="
                    px-4
                    py-2
                    font-medium
                    text-left text-gray-900
                    whitespace-nowrap
                  "
                >
                  Role
                </th>
                <th
                  class="
                    px-4
                    py-2
                    font-medium
                    text-left text-gray-900
                    whitespace-nowrap
                  "
                >
                  Salary
                </th>
              </tr>
            </thead>

            <tbody class="divide-y divide-gray-100">
              <tr>
                <td
                  class="px-4 py-2 font-medium text-gray-900 whitespace-nowrap"
                >
                  John Doe
                </td>
                <td class="px-4 py-2 text-gray-700 whitespace-nowrap">
                  24/05/1995
                </td>
                <td class="px-4 py-2 text-gray-700 whitespace-nowrap">
                  Web Developer
                </td>
                <td class="px-4 py-2 text-gray-700 whitespace-nowrap">
                  $120,000
                </td>
              </tr>

              <tr>
                <td class="px-4 py-2 font-medium whitespace-nowrap">
                  Jane Doe
                </td>
                <td class="px-4 py-2 text-gray-700 whitespace-nowrap">
                  04/11/1980
                </td>
                <td class="px-4 py-2 text-gray-700 whitespace-nowrap">
                  Web Designer
                </td>
                <td class="px-4 py-2 text-gray-700 whitespace-nowrap">
                  $100,000
                </td>
              </tr>

              <tr>
                <td class="px-4 py-2 font-medium whitespace-nowrap">
                  Gary Barlow
                </td>
                <td class="px-4 py-2 text-gray-700 whitespace-nowrap">
                  24/05/1995
                </td>
                <td class="px-4 py-2 text-gray-700 whitespace-nowrap">
                  Singer
                </td>
                <td class="px-4 py-2 text-gray-700 whitespace-nowrap">
                  $20,000
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../../components/SidebarAutoridad.vue";
import Navbar from "../../components/NavbarGeneral.vue";

export default {
  components: {
    Sidebar,
    Navbar,
  },
};
</script>

<style></style>
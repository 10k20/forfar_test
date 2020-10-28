<template>
<div class="wrapper">
    <label for="order">Your Order:</label><br>
    <textarea cols="60" rows="30" v-model="order"></textarea>
    <div class="point_list">
        <select v-model="printerID">
            <option disabled value="">Выберите printer id</option>
            <option v-for="printer in printers" :key="printer.id" :printerID="printer.id" :check_type="printer.check_type">{{ printer.id }} {{ printer.check_type }}</option>
        </select>
    </div>
    <div class="check_l">
        <button class="show_checks" v-on:click="getChecks()">Show Checks</button>
        <div class="checks" v-for="check in checks" :key="check.id" :id="check.id" :status="check.status" :type="check.type">
            {{ check.id }} {{ check.status }} {{ check.type }}
            <button v-on:click="renderCheck(check.id)">Rendered</button>
            <button v-on:click="printCheck(check.id)">Printed</button>
            <button v-on:click="deleteCheck(check.id)">Delete</button>
        </div>
    </div>
    <button class="add_check" v-on:click="postCheck()">Add Order</button>
</div>
</template>

<script>
export default {
    data() {
        return {
            checks: [],
            printers: [],
            order: '',
            printerID: '',
        }
    },
    asyncData({
        $axios,
        query
    }) {
        return Promise.all([
                $axios.get("http://localhost:8000/api/checks/"),
                $axios.get("http://localhost:8000/api/printers/"),
            ])
            .then(responses => {
                return {
                    checks: responses[0].data,
                    printers: responses[1].data
                };
            })
            .catch(e => {
                console.error(e);
            });
    },
    methods: {
        async getChecks() {
            const res = await this.$axios.$get("http://localhost:8000/api/checks/");
            this.checks = res;
        },
        async postCheck() {
            if (this.order != '' & this.printerID != '') {
                await this.$axios.$post("http://localhost:8000/api/checks/", {
                    type: 'kitchen',
                    order: this.order,
                    status: 'new',
                    printer_id: this.printerID,
                })
                await this.$axios.$post("http://localhost:8000/api/checks/", {
                    type: 'client',
                    order: this.order,
                    status: 'new',
                    printer_id: this.printerID,
                })
            } else {
                alert("Fill all fields")
            }
            this.getChecks()
        },
        async renderCheck(id) {
            await this.$axios.$patch("http://localhost:8000/api/checks/" + id + "/", {
                status: 'rendered',
            })
            await this.getChecks()
        },
        async printCheck(id) {
            await this.$axios.$patch("http://localhost:8000/api/checks/" + id + "/", {
                status: 'printed',
            })
            await this.getChecks()
        },
        async deleteCheck(id) {
            await this.$axios.$delete("http://localhost:8000/api/checks/" + id + "/")
            await this.getChecks()
        }

    }
}
</script>

<style lang="scss" scoped>
.wrapper {
    margin: 5vh 5vw;
}

.point_list {
    margin: 20px 0;
}

button {
    margin: 5px;
}
</style>

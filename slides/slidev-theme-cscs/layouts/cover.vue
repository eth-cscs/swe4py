<template>
  <div class="slidev-layout cover">
    <TitleTop />
    <div class="my-auto w-full below-header">
      <img :src="coverpic" class="banner"/>
      <slot />
    </div>
  </div>
</template>

<script setup>
const props = defineProps({coverpic: {default: "machine"}})
const coverpic = new URL("../assets/cover-" + props.coverpic + ".png", import.meta.url).href
</script>

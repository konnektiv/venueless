<template lang="pug">
.c-schedule-speakers
	bunt-progress-circular(v-if="!speakers || !schedule", size="huge", :page="true")
	.speakers(v-else)
		scrollbars(y="")
			router-link.speaker(v-for="speaker of speakers", :to="speaker.attendee ? {name: '', params: {}} : { name: 'schedule:speaker', params: { speakerId: speaker.code } }")
				img.avatar(v-if="speaker.avatar", :src="speaker.avatar")
				identicon(v-else, :id="speaker.name")
				.content
					.name {{ speaker.name }}
					p.biography {{ speaker.biography }} //- this has html ?
					.sessions
						.session(v-for="session of speaker.sessions")
							.title {{ session.title }}
</template>
<script>
// TODOs
// search
import { mapGetters, mapState } from 'vuex'

export default {
	data () {
		return {
			speakers: null
		}
	},
	computed: {
		...mapState('schedule', ['schedule']),
		...mapGetters('schedule', ['sessionsLookup'])
	},
	async created () {
		if (!this.$store.getters['schedule/pretalxApiBaseUrl']) return
		this.speakers = (await (await fetch(`${this.$store.getters['schedule/pretalxApiBaseUrl']}/speakers/?limit=999`)).json()).results.sort((a, b) => a.name.localeCompare(b.name))
		// const speakersToAttendee = await api.call('user.fetch', {pretalx_ids: this.speakers.map(speaker => speaker.code)})
		for (const speaker of this.speakers) {
			speaker.sessions = speaker.submissions.map(submission => this.sessionsLookup[submission])
			// speaker.attendee = speakersToAttendee[speaker.code]
		}
	},
	async mounted () {
		await this.$nextTick()
	},
	methods: {}
}
</script>
<style lang="stylus">
.c-schedule-speakers
	flex: auto
	min-height: 0
	display: flex
	flex-direction: column
	align-items: center
	.speakers
		flex: auto
		min-height: 0
		width: 100%
		max-width: 960px
		display: flex
		flex-direction: column
		gap: 8px
		border: border-separator()
		border-radius: 4px
		margin: 8px 4px
		.speaker
			color: $clr-primary-text-light
			display: flex
			gap: 8px
			cursor: pointer
			padding: 8px
			&:not(:last-child)
				border-bottom: border-separator()
			&:hover
				background-color: $clr-grey-200
			img
				flex: none
				border-radius: 50%
				height: 92px
				width: @height
				object-fit: cover
			.name
				font-weight: 500
				font-size: 16px
			.biography
				display: -webkit-box
				-webkit-box-orient: vertical
				-webkit-line-clamp: 3
				overflow: hidden
</style>
